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

pure bool hasDubs(immutable string text)
{
    return false;
}

void main()
{
    import std.stdio;
    import std.conv;

    string input = "hepxcrrq";

    assert(hasLoi("aeiou"));
    assert(!hasLoi("abcdefg"));

    assert(hasSeq("xabcy"));
    assert(!hasSeq("aeiou"));

    assert(hasDubs("xaabccy"));
    assert(!hasDubs("aaeiou"));

    writeln("Input: ", input);
}
