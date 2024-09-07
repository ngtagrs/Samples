package main

import (
	"flag"
	"fmt"
	"log"
	"math/rand"
	"net"
	"realtime-server/pb"
	"time"

	"google.golang.org/grpc"
)

var (
	port = flag.Int("port", 50051, "server port")
)

type RealtimeDataServiceServer struct {
	pb.UnimplementedRealtimeDataServiceServer
}

func (rfs *RealtimeDataServiceServer) StartRealtimeMarketFeed(request *pb.RealtimeMarketRequest, stream pb.RealtimeDataService_StartRealtimeMarketFeedServer) error {
	log.Printf("Client connected: %v", request.Ip)

	rand.Seed(time.Now().UnixNano())
	for {
		if err := stream.Context().Err(); err != nil {
			fmt.Printf("Client disconnected, stopping stream: %v", request.Ip)
			return err
		}

		equity_data_list := []*pb.EquityData{}
		equity_data := &pb.EquityData{
			Ticker: "AAA",
		}
		equity_data.SpotData = &pb.SpotData{
			Spot: rand.Float64(),
		}
		equity_data_list = append(equity_data_list, equity_data)

		if err := stream.Send(&pb.RealtimeMarketResponse{
			EquityDataList: equity_data_list,
		}); err != nil {
			return err
		}
		time.Sleep(time.Second * time.Duration(request.UpdateInterval))
	}
}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterRealtimeDataServiceServer(s, &RealtimeDataServiceServer{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
