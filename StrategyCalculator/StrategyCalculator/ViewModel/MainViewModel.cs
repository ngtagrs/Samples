
using StrategyCalculator.Model;
using StrategyCalculator.Model.Strategy;
using StrategyCalculator.Model.Strategy.Component;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace StrategyCalculator.ViewModel
{
    public partial class MainViewModel
    {
        private Strategy _strategy;
        private Options _options;

        public MainViewModel()
        {
            _strategy = new Strategy();
            _options = new Options();
        }

        public Strategy Strategy
        {
            get { return _strategy; }
        }

        public Options Options
        {
            get { return _options; }
        }
    }
}
