void main()
{
    import std.stdio;
    import std.string;
    import std.algorithm.iteration: permutations;
    import std.algorithm: canFind;
    import std.conv;
    import core.exception: RangeError;

    string[] locations;  // Unique list of locations
    int[string] paths;  // Assoc. array of costs for each route

    File input = File("input.txt", "r");
    while (!input.eof())
    {
        string line = strip(input.readln());
        if (line.length == 0)
            continue;

        string[] parts = line.split();
        if (!locations.canFind(parts[0]))
            locations ~= parts[0];
        if (!locations.canFind(parts[2]))
            locations ~= parts[2];

        paths[parts[0] ~ ":" ~ parts[2]] = to!int(parts[4]);
    }

    auto routes = locations.permutations;

    int shortest = 999_999;  // Part A
    int longest = 0;  // Part B
    foreach (route; routes)
    {
        int total_cost = 0;
        for (int i=0; i < route.length - 1; i++)
        {
            string leg;
            try
            {
                leg = route[i] ~ ":" ~ route[i + 1];
            }
            catch (RangeError e)
            {
                leg = route[i + 1] ~ ":" ~ route[i];
            }
            total_cost += paths[leg];
        }
        if (total_cost < shortest)
            shortest = total_cost;
        if (total_cost > longest)
            longest = total_cost;
    }
    writeln("Part A: %s - Shortest path cost", shortest);
    writeln("Part B: %s - Longest path cost", longest);
}
