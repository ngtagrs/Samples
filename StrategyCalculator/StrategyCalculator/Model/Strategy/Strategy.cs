using StrategyCalculator.Model.Strategy.Component;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json;
using System.Text.Json.Serialization;
using StrategyCalculator.Model.Base;

namespace StrategyCalculator.Model.Strategy
{
    public class Strategy : NotifyBase
    {
        private string _name;

        private ObservableCollection<Trade> _tradeList;
        private ObservableCollection<Position> _positionList;
        private ObservableCollection<Settlement> _settlementList;
        private ObservableCollection<Hedge> _hedgeList;

        private string _json;

        public Strategy()
        {
            _tradeList = new ObservableCollection<Trade>();
            _positionList = new ObservableCollection<Position>();
            _settlementList = new ObservableCollection<Settlement>();
            _hedgeList = new ObservableCollection<Hedge>();
        }

        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }
        public ObservableCollection<Trade> TradeList
        {
            get { return _tradeList; }
        }

        public ObservableCollection<Position> PositionList
        {
            get { return _positionList; }
        }
        public ObservableCollection<Settlement> SettlementList
        {
            get { return _settlementList; }
        }
        public ObservableCollection<Hedge> HedgeList
        {
            get { return _hedgeList; }
        }

        [JsonIgnore]
        public string Json
        {
            get { return _json; }
            set 
            {
                if (_json != value)
                {
                    _json = value;
                    RaisePropertyChanged("Json");
                }
            }
        }
    }
}
