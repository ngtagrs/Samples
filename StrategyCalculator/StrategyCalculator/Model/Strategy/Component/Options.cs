using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyCalculator.Model.Strategy.Component
{
    public class Options
    {
        private List<string> _underlying = new List<string> { "NIKKEI 225" };
        private string[] _tradeType = { "Option", "Future" };
        private string[] _optionType = { "European", "American" };
        private string[] _subType = { "Call", "Put" };
        private string[] _direction = { "Buy", "Sell" };
        private string[] _settlementType = { "SQ", "Reversing" };
        private string[] _hedgeTarget = { "Delta", "Vega" };
        private string[] _hedgeTradeType = { "Future", "Cash", "STRD" };

        public List<string> Underlying { get { return _underlying; } }
        public string[] TradeType { get { return _tradeType; } }
        public string[] OptionType { get { return _optionType; } }
        public string[] SubType { get { return _subType; } }
        public string[] Direction { get { return _direction; } }
        public string[] SettlementType { get { return _settlementType; } }
        public string[] HedgeTarget { get { return _hedgeTarget; } }
        public string[] HedgeTradeType { get { return _hedgeTradeType; } }
    }
}
