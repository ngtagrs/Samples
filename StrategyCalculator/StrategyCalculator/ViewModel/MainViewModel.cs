using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrategyCalculator.ViewModel
{
    public class MainViewModel
    {
        private Dictionary<string, List<double>> _testDic1;
        private ObservableDictionary<string, List<double>> _testDic2;

        public MainViewModel()
        {
            _testDic1 = new Dictionary<string, List<double>>();
            _testDic2 = new ObservableDictionary<string, List<double>>();
            _testDic1.Add("1", new List<double>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, });
            _testDic2.Add("1", new List<double>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, });
        }

        public Dictionary<string, List<double>> TestDic1 { get {  return _testDic1; } }
        public ObservableDictionary<string, List<double>> TestDic2 { get { return _testDic2; } }  
    }
}
