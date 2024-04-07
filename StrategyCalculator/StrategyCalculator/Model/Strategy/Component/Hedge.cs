using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyCalculator.Model.Strategy.Component
{
    public class Hedge
    {
        public string Target { get; set; }
        public string TradeType { get; set; }
        public string DateCondition { get; set; }
        public TimeSpan Time { get; set; }
    }
}
