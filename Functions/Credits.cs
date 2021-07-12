using Console = Colorful.Console;
using System.Drawing;
using Shock;

namespace Shock.Functions
{
    internal class credits
    {
        public static void creds()
        {
            System.Console.Clear();
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.2 | vx#1234 [<]";
            Console.WriteLine("");
            Program.Ascii();
            Console.WriteLine("");
            prefix("+", "KyeOnDiscord - For making a proxy scraper that was very easy to expand on\n");
            prefix("+", "0cw - For developing BoltAIO which is the main base for this program  \n");
            prefix("+", "Her - Getting banned from c.to which allowed their c.to auth to get cracked lol (Hulu Checker)\n");
            prefix("+", "NightfallGT - For developing a insanely overpowered nordvpn checker\n");
            prefix("+", "JayJay#0124 - For helping me debug\n");
            prefix("+", "! 0xluxiferr#0001 - For helping me learn how to call python scripts inside a C# application\n");
            Console.WriteLine(" ");
            Console.WriteLine(" ");
            prefix(">", " ");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                default:
                    Program.Menu0();
                    break;
            }
        }
        public static void prefix(string prefix, string description)
        {
            Console.Write("    [", Color.White);
            Console.Write(prefix, Color.Cyan);
            Console.Write("] " + description, Color.White);
        }
    }
}