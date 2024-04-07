using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace StrategyCalculator.Model.Gpt
{
    public class GptClient : IDisposable
    {
        private string _url = "https://api.openai.com/v1/chat/completions";
        private string _apiKey = "";
        private string _model = "gpt-3.5-turbo";

        private HttpClient _httpClient;

        public GptClient(int apiTimeout_=60)
        {
            _httpClient = new HttpClient()
            {
                Timeout = TimeSpan.FromSeconds(apiTimeout_)
            };
        }

        public void Chat(string message_, Dictionary<string, string> history_)
        {

        }

        public void Dispose()
        {
            _httpClient.Dispose();
        }
    }
}
