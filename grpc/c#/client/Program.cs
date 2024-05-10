using Calculator;
using Dummy;
using Greet;
using Grpc.Core;
using Sqrt;

namespace client
{
    internal class Program
    {
        const string target = "127.0.0.1:50051";
        static async Task Main(string[] args)
        {
            var clientCert = File.ReadAllText("ssl/client.crt");
            var clientKey = File.ReadAllText("ssl/client.key");
            var caCrt = File.ReadAllText("ssl/ca.crt");

            var channelCredential = new SslCredentials(caCrt, new KeyCertificatePair(clientCert, clientKey));

            Channel channel = new Channel("localhost", 50051, channelCredential);

            await channel.ConnectAsync().ContinueWith((task) =>
            {
                if (task.Status == TaskStatus.RanToCompletion)
                    Console.WriteLine("The client connected successfully");
            });

            await UnaryGreeting(channel);
            //await ServerStreamingGreeting(channel);
            //await ClientStreamingGreeting(channel);
            //await BidiGreeting(channel);
            //await DeadlineGreeting(channel);
            //await UnaryCalculate(channel);
            //await ServerStreamingCalculate(channel);
            //await ClientStreamingCalculate(channel);
            //await BidiStreamingCalculate(channel);
            //await Sqrt(channel);

            channel.ShutdownAsync().Wait();
            Console.ReadKey();
        }

        private async static Task UnaryGreeting(Channel channel)
        {
            var client = new GreetingService.GreetingServiceClient(channel);

            var greeting = new Greeting()
            {
                FirstName = "Nobuhiro",
                LastName = "Nagata"
            };

            var request = new GreetingRequest() { Greeting = greeting };
            var response = client.Greet(request);

            Console.WriteLine(response.Result);
        }

        private async static Task ServerStreamingGreeting(Channel channel)
        {
            var client = new GreetingService.GreetingServiceClient(channel);

            var greeting = new Greeting()
            {
                FirstName = "Nobuhiro",
                LastName = "Nagata"
            };

            var request = new GreetingManyTimesRequest() { Greeting = greeting };
            var response = client.GreetManyTimes(request);

            while (await response.ResponseStream.MoveNext())
            {
                Console.WriteLine(response.ResponseStream.Current.Result);
                await Task.Delay(200);
            }
        }

        private async static Task ClientStreamingGreeting(Channel channel)
        {
            var client = new GreetingService.GreetingServiceClient(channel);

            var greeting = new Greeting()
            {
                FirstName = "Nobuhiro",
                LastName = "Nagata"
            };

            var request = new LongGreetRequest() { Greeting = greeting };
            var stream = client.LongGreet();
            foreach (int i in Enumerable.Range(0, 10))
            {
                await stream.RequestStream.WriteAsync(request);
            }

            await stream.RequestStream.CompleteAsync();

            var response = await stream.ResponseAsync;
            Console.WriteLine(response.Result);
        }

        private async static Task BidiGreeting(Channel channel)
        {
            var client = new GreetingService.GreetingServiceClient(channel);

            var stream = client.GreetEveryone();

            var responseReaderTask = Task.Run(async () =>
            {
                while (await stream.ResponseStream.MoveNext())
                {
                    Console.WriteLine("Received : " + stream.ResponseStream.Current.Result);
                }
            });

            Greeting[] greetings =
            {
                new Greeting() { FirstName = "John", LastName="Doe"},
                new Greeting() { FirstName = "Clement", LastName="Jean"},
                new Greeting() { FirstName = "Patricia", LastName="Hertz"},
            };

            foreach(var greeting in greetings) 
            {
                Console.WriteLine($"Sending : " + greeting.ToString());
                await stream.RequestStream.WriteAsync(new GreetEveryoneRequest()
                {
                    Greeting = greeting
                });
            }

            await stream.RequestStream.CompleteAsync();
            await responseReaderTask;
        }

        private static async Task DeadlineGreeting(Channel channel)
        {
            var client = new GreetingService.GreetingServiceClient(channel);

            try
            {
                var response = client.GreetWithDeadline(new GreetingDeadlineRequest() { Name = "John" }, deadline:DateTime.UtcNow.AddMilliseconds(100));
                Console.WriteLine(response.Result);
            }
            catch(RpcException e) when (e.StatusCode == StatusCode.DeadlineExceeded)
            {
                Console.WriteLine($"Error : {e.Status.Detail}");
            }
        }

        private async static Task UnaryCalculate(Channel channel)
        {
            var client = new CalculatorService.CalculatorServiceClient(channel);

            var request = new CalculateRequest() { Value1=2, Value2=10 };
            var response = client.Calculate(request);
            Console.WriteLine($"{response.Answer}");
        }

        private async static Task ServerStreamingCalculate(Channel channel)
        {
            var client = new CalculatorService.CalculatorServiceClient(channel);

            var request = new PrimeNumberDecompositionRequest() { N = 100 };
            var response = client.PrimeNumberDecompose(request);
            while (await response.ResponseStream.MoveNext())
            {
                Console.WriteLine(response.ResponseStream.Current.PrimeNumber);
                await Task.Delay(200);
            }
        }

        private async static Task ClientStreamingCalculate(Channel channel)
        {
            var client = new CalculatorService.CalculatorServiceClient(channel);

            var stream = client.ComputeAverage();
            foreach(int i in Enumerable.Range(0, 100))
            {
                var request = new ComputeAverageRequest() { N = i };
                await stream.RequestStream.WriteAsync(request);
            }

            await stream.RequestStream.CompleteAsync();

            var response = stream.ResponseAsync;
            Console.WriteLine(response.Result);
        }

        private static async Task BidiStreamingCalculate(Channel channel)
        {
            var client = new CalculatorService.CalculatorServiceClient(channel);

            var stream = client.CurrentMaximum();

            var responseTask = Task.Run(async () =>
            {
                while (await stream.ResponseStream.MoveNext())
                {
                    var maximum = stream.ResponseStream.Current.Maximum;
                    Console.WriteLine(maximum);
                }
            });

            var numbers = new int[] { 1, 5, 3, 6, 2, 20};
            foreach (int i in  numbers)
            {
                await stream.RequestStream.WriteAsync(new CurrentMaximumRequest() { N = i });
            }

            await stream.RequestStream.CompleteAsync();
            await responseTask;
        }

        private static async Task Sqrt(Channel channel)
        {
            var client = new SqrtService.SqrtServiceClient(channel);

            int number = -1;

            try
            {
                var response = client.sqrt(new SqrtRequest() { Number = number });

                Console.WriteLine(response.SquareRoot);
            }
            catch (RpcException e)
            {
                Console.WriteLine("Error : " + e.Status.Detail);
            }
        }
    }
}
