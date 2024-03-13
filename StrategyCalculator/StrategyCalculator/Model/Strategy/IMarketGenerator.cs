using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyCalculator.Model
{
    public interface IMarketGenerator
    {
        Dictionary<string, Dictionary<string, double>> Generate(IEnumerable<TradeData> trades_);
    }
}
