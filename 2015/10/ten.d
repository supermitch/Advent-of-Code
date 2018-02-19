import std.conv;

pure string expand(immutable(string) input)
{
    string output = "";
    char curr = input[0];
    int count = 1;
    foreach (c; input[1 .. $])
    {
        if (c == curr)
        {
            count += 1;
        }
        else
        {
            output ~= to!string(count) ~ to!string(curr);
            curr = c;
            count = 1;
        }
    }
    output ~= to!string(count) ~ to!string(curr);
    return output;
}

void main()
{
    import std.stdio;

    string input = "1113222113";
    foreach (i; 0..50)
    {
        input = expand(input);
        if (i == 39)
            writefln("Part A: %s - Length after 40 iterations", input.length);
    }
    writefln("Part B: %s - Length after 50 iterations", input.length);
}
