using System;
using System.Linq;

namespace AnagramDetection
{
  class AnagramDetection
  {
    static void Main(string[] args)
    {
      Console.WriteLine(_Occurences("AdnBndAndBdaBn", "dAn"));
      Console.WriteLine(_Occurences("AbrAcadAbRa", "cAda"));
      Console.ReadKey();
    }


    private static int _Occurences(string parent, string child)
    {
      int occurences = 0;
      if (child.Length > parent.Length)
        return 0;

      for (int i = 0; i <= (parent.Length - child.Length); i++)
      {
        var parentSub = parent.Substring(i, child.Length);

        if (_IsAnagram(parentSub, child))
          occurences++;
      }
      return occurences;
    }


    private static bool _IsAnagram(string s, string t)
    {
      return s.OrderBy(c => c).SequenceEqual(t.OrderBy(c => c));
    }


    private static bool _IsAnagram2(string s, string t)
    {

      for (int i = 0; i < t.Length; i++)
      {
        var n = s.IndexOf(t[i]);
        if (n < 0)
          return false;
        s = s.Remove(n, 1);
      }
      return String.IsNullOrEmpty(s);
    }

  }
}
