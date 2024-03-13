using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyCalculator.Model
{
    public class Strategy
    {

    }
    public class TimeTrade
    {
        public string Time { get; set; }
        public Condition Condition { get; set; }
        public List<Process> Processes { get; set; }
        public bool IsBbgImport { get; set; }
        public bool IsBookToMurex { get; set; }
    }

    public class Condition
    {
        public string Type { get; set; }
        public string SpotReferenceTime { get; set; }
        public string TradeType { get; set; }
        // 他にも条件や数式などを追加
    }

    public class Process
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Type { get; set; }
        public string Description { get; set; }
    }
}
