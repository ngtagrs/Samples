using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyCalculator.Model.Strategy.Component
{
    public class Trade
    {
        public string Underlying { get; set; }
        public string TradeType { get; set; }
        public string OptionType { get; set; }
        public string SubType { get; set; }
        public double StrikeRatio { get; set; }
        public string MaturityTenor { get; set; }
        public string TradeDirection { get; set; }

    }
}
