BEGIN {
    tcp = 0;
    udp = 0;
} {
    event = $5;
    if(event == "cbr")
        udp++;
    if(event == "tcp")
        tcp++;
} END {
    printf("Number of TCP packets: %d\n", tcp);
    printf("Number of UDP packets: %d\n", udp);
}