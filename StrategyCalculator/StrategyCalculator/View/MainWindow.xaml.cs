using StrategyCalculator.Model;
using StrategyCalculator.View.Controls;
using StrategyCalculator.ViewModel;
using System.Collections.ObjectModel;
using System.Windows;

namespace StrategyCalculator
{
    public partial class MainWindow : Window
    {
        public ObservableCollection<TimeTrade> TimeTrades { get; set; }

        public MainWindow()
        {
            InitializeComponent();
            TimeTrades = new ObservableCollection<TimeTrade>();
            DataContext = new MainViewModel();
        }

        private void AddTimeTradeButton_Click(object sender, RoutedEventArgs e)
        {
            // ボタンがクリックされたときの処理
            this.TimePanel.Children.Add(new TimeBox());
            //TimeTrades.Add(new TimeTrade { Time = "新しい時間", Conditions = new List<Model.Condition>() });
        }

        private void RemoveTimeTradeButton_Click(object sender, RoutedEventArgs e)
        {
            // ボタンがクリックされたときの処理
            //if (timeTradesListBox.SelectedItem is TimeTrade selectedTimeTrade)
            //{
            //    TimeTrades.Remove(selectedTimeTrade);
            //}
        }

        private void CalculateButton_Click(object sender, RoutedEventArgs e)
        {
            // ボタンがクリックされたときの処理
            // 例: ユーザーが選択したトレードの時間や条件を取得し、計算エンジンに渡す
            // そして、計算結果を表示する
            resultTextBox.Text = "計算結果がここに表示されます。";
        }

        private void AddTradeButton_Click(object sender, RoutedEventArgs e)
        {
            this.TradePanel.Children.Add(new TradeBox());
        }

        private void AddParameterDefinitionButton_Click(object sender, RoutedEventArgs e)
        {

        }

        private void UpdateTabButton_Click(object sender, RoutedEventArgs e)
        {
            var cnt = ((MainViewModel)this.DataContext).TestDic1.Count;
            ((MainViewModel)this.DataContext).TestDic1.Add($"{cnt+1}", new List<double>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, });
            ((MainViewModel)this.DataContext).TestDic2.Add($"{cnt + 1}", new List<double>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, });
        }
    }
}
