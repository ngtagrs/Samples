using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace StrategyCalculator.View.Controls
{
    /// <summary>
    /// TradeBox.xaml の相互作用ロジック
    /// </summary>
    public partial class TradeBox : UserControl
    {
        public TradeBox()
        {
            InitializeComponent();

            var categoryList = new List<string>();
            categoryList.Add("Equity");
            categoryList.Add("FX");
            categoryList.Add("IR");
            categoryList.Add("Bond");
            categoryList.Add("Credit");
            this.CategoryComboBox.ItemsSource = categoryList;

            var tradeTypeList = new List<string>();
            tradeTypeList.Add("Cash");
            tradeTypeList.Add("Future");
            tradeTypeList.Add("Option");
            this.TradeTypeComboBox.ItemsSource = tradeTypeList;

            var optionTypeList = new List<string>();
            optionTypeList.Add("European");
            optionTypeList.Add("American");
            this.OptionTypeComboBox.ItemsSource = optionTypeList;

            var subTypeList = new List<string>();
            subTypeList.Add("Call");
            subTypeList.Add("Put");
            this.SubTypeComboBox.ItemsSource = subTypeList; 
        }

        private void DeleteButton_Click(object sender, RoutedEventArgs e)
        {
            
        }
    }
}
