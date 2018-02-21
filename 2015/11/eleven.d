import std.stdio;

pure bool hasLoi(immutable string text)
{
    import std.algorithm : canFind;
    return text.canFind("l") || text.canFind("o") || text.canFind("i");
}

pure bool hasSeq(immutable string text)
{
    import std.conv : to;
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

bool hasDubs(immutable string text)
{
    import std.algorithm : chunkBy;
    import std.conv : to;

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

void main()
{

    string input = "hepxcrrq";

    assert(hasLoi("aeiou"));
    assert(!hasLoi("abcdefg"));

    assert(hasSeq("xabcy"));
    assert(!hasSeq("aeiou"));

    assert(hasDubs("xaabccy"));
    assert(!hasDubs("aaeiou"));
    assert(!hasDubs("aaaiou"));
    assert(!hasDubs("aaaiaa"));
    assert(!hasDubs("abcdef"));

    writeln("Input: ", input);
}
