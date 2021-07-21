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
                "                                                                                                       [>] Shock | Version 1.8 | vx#1234 [<]";
            Console.WriteLine("");
            Program.Ascii();
            Console.WriteLine("");
            Program.prefix("+", "github.com/KyeOnDiscord - Proxy Scraper\n");
            Program.prefix("+", "Quanotics#8507 - Shock's Base (BoltAIO V2)\n");
            Program.prefix("+", "c.to/Her - Hulu Checker\n");
            Program.prefix("+", "github.com/NightfallGT - NordVPN Checker\n");
            Program.prefix("+", "! 0xluxiferr#0132 - Calling python scripts inside C#\n");
            Program.prefix("+", "xshonda#9999 - ShockAIO's Showcase Video (Got Taken Down RIP)\n");

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