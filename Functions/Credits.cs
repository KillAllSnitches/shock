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
                "                                                                                                       [>] Shock | Version 1.4 | vx#1234 [<]";
            Console.WriteLine("");
            Program.Ascii();
            Console.WriteLine("");
            Program.prefix("+", "KyeOnDiscord - Proxy Scraper\n");
            Program.prefix("+", "0cw - Shock's Base (BoltAIO V2)\n");
            Program.prefix("+", "Her - Hulu Checker\n");
            Program.prefix("+", "NightfallGT - NordVPN Checker\n");
            Program.prefix("+", "luxiferr - Calling python scripts inside C#\n");
            Program.prefix("+", "xshonda - ShockAIO's Showcase Video\n");

            Console.WriteLine(" ");
            Console.WriteLine(" ");
            Program.prefix(">", " ");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                default:
                    Program.Menu0();
                    break;
            }
        }
    }
}