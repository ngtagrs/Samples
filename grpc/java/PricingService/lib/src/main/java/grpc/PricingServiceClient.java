package grpc;

import grpc.PricingServiceOuterClass.PricingRequest;
import grpc.PricingServiceOuterClass.PricingResponse;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class PricingServiceClient {
	public static void main(String[] args) {
		ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 50051)
				.usePlaintext()
				.build();
		PricingServiceGrpc.PricingServiceBlockingStub blockingStub = PricingServiceGrpc.newBlockingStub(channel);
		
		PricingRequest request = PricingRequest.newBuilder().setRequest("Nobu").build();
		PricingResponse response = blockingStub.pricing(request);
		
		System.out.println(response.getResponse());
	}
}
