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
    /// TimeBox.xaml の相互作用ロジック
    /// </summary>
    public partial class TimeBox : UserControl
    {
        public TimeBox()
        {
            InitializeComponent();

            var timeList = new List<TimeSpan>();
            timeList.Add(new TimeSpan(7, 0, 0));
            timeList.Add(new TimeSpan(8, 0, 0));
            timeList.Add(new TimeSpan(9, 0, 0));
            timeList.Add(new TimeSpan(10, 0, 0));
            this.TimeComboBox.ItemsSource = timeList;
        }
    }
}
