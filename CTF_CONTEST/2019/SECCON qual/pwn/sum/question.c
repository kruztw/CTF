void main()
{
    input = 0;
    local_40 = 0;
    local_38 = 0;
    local_30 = 0;
    local_28 = 0;
    i = 0;
    total = &i;
    puts("[sum system]\nInput numbers except for 0.\n0 is interpreted as the end of sequence.\n");
    puts("[Example]\n2 3 4 0");
    read_ints(&input, 5);
    input_num = sum(&input, total);
    if (5 < input_num)
        exit(-1);

    printf("%llu\n",i);

    return 0;
}


ulong sum(long input,long *total)
{ 
    *total = 0;
    for(int i = 0; input[i]; i++)
        *total += input[i];

    return (ulong)i;
}


void read_ints(long input,long num)
{  
    for(int i = 0; i<= num; i++){
        if (scanf("%lld", input[i]) != 1) 
            exit(-1);
        if(!input[i]) break;
    }
}
