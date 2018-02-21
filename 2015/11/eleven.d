import std.conv : to;
import std.stdio;

pure bool hasLoi(immutable char[] text)
{
    import std.algorithm : canFind;
    return text.canFind("l") || text.canFind("o") || text.canFind("i");
}

pure bool hasSeq(immutable char[] text)
{
    for (int i=0; i < text.length - 2; i++)
    {
        int a = to!int(text[i]);
        int b = to!int(text[i + 1]);
        int c = to!int(text[i + 2]);
        if (a + 2 == b + 1 && b + 1 == c)
            return true;
    }
    return false;
}

pure bool hasDubs(immutable char[] text)
{
    import std.algorithm : chunkBy;

    string first_group = "";
    auto chunks = chunkBy!(c => c)(text);
    foreach (g; chunks) {
        string val = to!string(g[1]);
        if (val.length >= 2)
        {
            if (first_group == "")
                first_group = val[0..2];
            else if (val != first_group)
                return true;
        }
    }
    return false;
}


int[] increment(int[] nums, ulong pos)
{
    nums[pos] = (nums[pos] - 97 + 1) % 26 + 97;
    if (nums[pos] == 97)
        nums = increment(nums, pos - 1);
    return nums;
}

void main()
{

    string partA = "hepxcrrq";
    string partB = "hepxxyzz";

    assert(hasLoi("aeiou"));
    assert(!hasLoi("abcdefg"));

    assert(hasSeq("xabcy"));
    assert(!hasSeq("aeiou"));

    assert(hasDubs("xaabccy"));
    assert(!hasDubs("aaeiou"));
    assert(!hasDubs("aaaiou"));
    assert(!hasDubs("aaaiaa"));
    assert(!hasDubs("abcdef"));

    import std.algorithm : map;
    import std.array;
    auto nums = map!(a => to!int(a))(partA).array;
    auto chars = map!(a => to!char(a))(nums).array;
    while (true) {
        nums = increment(nums, nums.length - 1);
        chars = map!(a => to!char(a))(nums).array;
        if (!hasLoi(to!string(chars)) && hasSeq(to!string(chars)) && hasDubs(to!string(chars)))
            break;
    }
    writeln("Part A: ", chars);

    nums = map!(a => to!int(a))(partB).array;
    while (true) {
        nums = increment(nums, nums.length - 1);
        chars = map!(a => to!char(a))(nums).array;
        if (!hasLoi(to!string(chars)) && hasSeq(to!string(chars)) && hasDubs(to!string(chars)))
            break;
    }
    writeln("Part B: ", chars);
}
