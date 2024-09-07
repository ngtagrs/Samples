using Grpc.Core;
using Grpc.Net.Client;
using RealtimeMarketService;
using System.Net;
using System.Net.Sockets;
using static RealtimeMarketService.RealtimeDataService;

namespace RealtimeFeedClient
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            var interval = int.Parse(args[0]);

            using (var channel = GrpcChannel.ForAddress("http://localhost:50051"))
            {
                var client = new RealtimeDataServiceClient(channel);

                IPHostEntry host = Dns.GetHostEntry(Dns.GetHostName());
                var ippaddress = host.AddressList.FirstOrDefault(ip => ip.AddressFamily == AddressFamily.InterNetwork);

                var request = new RealtimeMarketRequest { Ip = ippaddress?.ToString(), UpdateInterval = interval };
                using (var call = client.StartRealtimeMarketFeed(request))
                {
                    await foreach (var response in call.ResponseStream.ReadAllAsync())
                    {
                        foreach(var equityData in response.EquityDataList)
                        {
                            Console.WriteLine($"{equityData.Ticker} : {equityData.SpotData.Spot}");
                        }
                    }
                }
            }
        }
    }
}
