using Calculator;
using Grpc.Core;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static Calculator.CalculatorService;

namespace server
{
    public class CalculatorServiceImpl : CalculatorServiceBase
    {
        public override Task<CalculateResponse> Calculate(CalculateRequest request, ServerCallContext context)
        {
            return Task.FromResult(new CalculateResponse() { Answer = request.Value1 + request.Value2 });
        }

        public override async Task PrimeNumberDecompose(PrimeNumberDecompositionRequest request, IServerStreamWriter<PrimeNumberDecompositionResponse> responseStream, ServerCallContext context)
        {
            int n = request.N;
            int k = 2;
            while (n > 1)
            {
                if(n % k == 0)
                {
                    await responseStream.WriteAsync(new PrimeNumberDecompositionResponse() { PrimeNumber = k } );
                    n /= k;
                }
                else
                {
                    k++;
                }
            }
        }

        public override async Task<ComputeAverageResponse> ComputeAverage(IAsyncStreamReader<ComputeAverageRequest> requestStream, ServerCallContext context)
        {
            var sum = 0;
            while (await requestStream.MoveNext())
            {
                var n = requestStream.Current.N;
                sum += n;
            }
            return new ComputeAverageResponse() { Average = sum };
        }

        public override async Task CurrentMaximum(IAsyncStreamReader<CurrentMaximumRequest> requestStream, IServerStreamWriter<CurrentMaximumResponse> responseStream, ServerCallContext context)
        {
            int maximum = 0;
            while(await requestStream.MoveNext())
            {
                int n = requestStream.Current.N;
                Console.WriteLine("Received : " + n);
                maximum = Math.Max(maximum, n);
                await responseStream.WriteAsync(new CurrentMaximumResponse() { Maximum = maximum });
            }
        }
    }
}
