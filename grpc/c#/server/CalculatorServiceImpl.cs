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
    }
}
