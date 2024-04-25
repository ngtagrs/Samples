using Calculator;
using Dummy;
using Greet;
using Grpc.Core;

namespace client
{
    internal class Program
    {
        const string target = "127.0.0.1:50051";
        static async Task Main(string[] args)
        {
            Channel channel = new Channel(target, ChannelCredentials.Insecure);

            await channel.ConnectAsync().ContinueWith((task) =>
            {
                if (task.Status == TaskStatus.RanToCompletion)
                    Console.WriteLine("The client connected successfully");
            });

            //var client = new DummyService.DummyServiceClient(channel);
            var client = new GreetingService.GreetingServiceClient(channel);

            var greeting = new Greeting()
            {
                FirstName = "Nobuhiro",
                LastName = "Nagata"
            };

            //var request = new GreetingRequest() { Greeting = greeting };
            //var response = client.Greet(request);

            //Console.WriteLine(response.Result);

            var request = new GreetingManyTimesRequest() { Greeting = greeting };
            var response = client.GreetManyTimes(request);

            while (await response.ResponseStream.MoveNext())
            {
                Console.WriteLine(response.ResponseStream.Current.Result);
                await Task.Delay(200);
            }

            //var calculatorClient = new CalculatorService.CalculatorServiceClient(channel);
            //var calculationRequest = new CalculateRequest() { Value1 = 2, Value2 = 3 };
            //var calculatorResponse = calculatorClient.Calculate(calculationRequest);
            //Console.WriteLine($"{calculatorResponse.Answer}");

            channel.ShutdownAsync().Wait();
            Console.ReadKey();
        }
    }
}
