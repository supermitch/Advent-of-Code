void main()
{
    import std.stdio;
    import std.string;

    File input = File("input.txt", "r");
    int[] lines = new int[300];  // Length of input.txt

    int difference = 0;  // Part A
    ulong encoded = 0;  // Part B

    while (!input.eof())
    {
        string line = strip(input.readln());

        difference += 2;  // Include surrounding quotes
        for (int i = 1; i < (line.length - 2); i++)
        {
            string piece = line[i..i+2];
            if (piece == "\\\\" || piece == "\\\"")
            {
                difference += 1;
                i += 1;
            }
            else if (piece == "\\x")  // e.g. /xF4
            {
                difference += 3;
                i += 3;
            }
        }

        encoded += count(line, "\"") + count(line, "\\") + 2;  // 2 includes new quotes
    }

    writefln("Part A: %s - Difference between chars and literals", difference);
    writefln("Part B: %s - Difference between encoded strings", encoded);
}
