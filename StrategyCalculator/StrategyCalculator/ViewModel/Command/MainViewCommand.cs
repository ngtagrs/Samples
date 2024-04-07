using StrategyCalculator.Model.Strategy.Component;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Windows.Input;

namespace StrategyCalculator.ViewModel
{
    public class Command : ICommand
    {
        public event EventHandler? CanExecuteChanged;
        private Action _action;

        public Command(Action action_)
        {
            _action = action_;
        }

        public bool CanExecute(object? parameter)
        {
            return true;
        }

        public void Execute(object? parameter)
        {
            _action();
        }
    }
    public partial class MainViewModel
    {
        private ICommand _addTradeCommand;
        public ICommand AddTradeCommand
        {
            get { return _addTradeCommand ?? (_addTradeCommand = new Command(AddTradeCommand_CallBack)); }
        }

        private void AddTradeCommand_CallBack()
        {
            _strategy.TradeList.Add(new Trade());
        }

        private ICommand _addPositionCommand;
        public ICommand AddPositionCommand
        {
            get { return _addPositionCommand ?? (_addPositionCommand = new Command(AddPositionCommand_CallBack)); }
        }

        private void AddPositionCommand_CallBack()
        {
            _strategy.PositionList.Add(new Position());
        }

        private ICommand _addSettlementCommand;
        public ICommand AddSettlementCommand
        {
            get { return _addSettlementCommand ?? (_addSettlementCommand = new Command(AddSettlementCommand_CallBack)); }
        }

        private void AddSettlementCommand_CallBack()
        {
            _strategy.SettlementList.Add(new Settlement());
        }

        private ICommand _addHedgeCommand;
        public ICommand AddHedgeCommand
        {
            get { return _addHedgeCommand ?? (_addHedgeCommand = new Command(AddHedgeCommand_CallBack)); }
        }

        private void AddHedgeCommand_CallBack()
        {
            _strategy.HedgeList.Add(new Hedge());
        }

        private ICommand _convertToJsonCommand;
        public ICommand ConvertToJsonCommand
        {
            get { return _convertToJsonCommand ?? (_convertToJsonCommand = new Command(ConvertToJsonCommand_CallBack)); }
        }

        private void ConvertToJsonCommand_CallBack()
        {
            var options = new JsonSerializerOptions { WriteIndented = true };
            _strategy.Json = System.Text.Json.JsonSerializer.Serialize(_strategy, options);
        }
    }
}
