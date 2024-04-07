using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyCalculator.Model.Strategy.Component
{
    public class Settlement
    {
        public string Type { get; set; }
        public string DateCondition { get; set; }
        public TimeSpan Time { get; set; }
    }
}
