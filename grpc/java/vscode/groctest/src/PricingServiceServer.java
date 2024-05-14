class PricingServiceServer {
    public static void main(String[] args) {
        Server server = ServerBuilder.forPort(50050).addService(new PricingServiceImpl()).build();
    }
}