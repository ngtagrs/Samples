package grpc;

import java.io.IOException;

import io.grpc.Server;
import io.grpc.ServerBuilder;

public class PricingServiceServer {
	public static void main(String[] args) throws IOException, InterruptedException {
		System.out.println("Start PricingServiceServer");
		
		Server server = ServerBuilder.forPort(50051)
				.addService(new PricingServiceImpl())
				.build()
				.start();
		
		Runtime.getRuntime().addShutdownHook(new Thread(server::shutdown));
		
		server.awaitTermination();
	}
}
