using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Net;
using System.Windows.Forms;
using Shock.Modules;
using Shock.Functions;
using System.Text;
using Console = Colorful.Console;

namespace Shock
{
    internal class Program
    {
        private static readonly List<Action> PickedModules = new List<Action>();
        public static int Fails = 0;
        public static int Hits = 0;
        public static int Frees = 0;
        public static int Errors = 0;
        public static int TotalChecks = 0;
        public static int Others = 0;
        public static int Cpm;
        public static string ProxyType1 = "";
        public static string lorc = "";
        private static readonly OpenFileDialog Ofd = new OpenFileDialog();
        public static List<string> Proxies = new List<string>();
        public static List<string> Combos = new List<string>();
        public static int Proxytotal;
        public static int Combostotal;
        public static int Threads;
        public static int Stop = 0;
        public static int Proxyindex = 0;
        public static int Combosindex = 0;
        public static bool CheckerRunning;


        public static string RequestUriString { get; set; }
        public static void prefix(string prefix, string description)
        {
            Console.Write("    [", Color.White);
            Console.Write(prefix, Color.Cyan);
            Console.Write("] " + description, Color.White);
        }

        private static void Main(string[] args)
        {
            Menu0();
        }

        public static void Ascii()
        {
            System.Console.Clear();
            Console.Clear();
            Console.WriteLine("");
            Console.WriteLine("                                 ▄▀▀▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▄▄▄▄   ▄▀▀▄ █ ",
                Color.Cyan);
            Console.WriteLine("                                █ █   ▐ █  █   ▄▀ █      █ █ █    ▌ █  █ ▄▀ ",
                Color.Cyan);
            Console.WriteLine("                                   ▀▄   ▐  █▄▄▄█  █      █ ▐ █      ▐  █▀▄  ",
                Color.Cyan);
            Console.WriteLine("                                ▀▄   █     █   █  ▀▄    ▄▀   █        █   █ ",
                Color.Cyan);
            Console.WriteLine("                                 █▀▀▀     ▄▀  ▄▀    ▀▀▀▀    ▄▀▄▄▄▄▀ ▄▀   █  ",
                Color.Cyan);
            Console.WriteLine("                                 ▐       █   █             █     ▐  █    ▐  ",
                Color.Cyan);
            Console.WriteLine("                                          ▐   ▐             ▐        ▐       ",
                Color.Cyan);
            Console.WriteLine("");
            Console.WriteLine("                                Join Shock's Discord - discord.io/shockaio", Color.White);
            Console.WriteLine("");
        }
        public static void Menu0()
        {
            DiscordRPC1.Initialize();
            Export.Initialize();
            menu1:
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.8 | vx#1234 [<]";
            Ascii();
            System.Console.ForegroundColor = ConsoleColor.Cyan;
            prefix("1", "Combo Tools\n");
            prefix("2", "Checkers\n");
            prefix("3", "SQLi Tools\n");
            prefix("4", "Other Tools\n");
            prefix("5", "Credits\n");
            Console.WriteLine("");
            Console.WriteLine("");
            prefix(">", "");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                case "1":
                    {
                        combotools();
                        break;
                    }
                case "2":
                    {
                        checkers();
                        break;
                    }
                case "3":
                    {
                        sqltools();
                        break;
                    }
                case "4":
                    {
                        misc();
                        break;
                    }
                case "5":
                    {
                        credits.creds();
                        break;
                    }
                default:
                    prefix("Invalid Option", "");
                    Thread.Sleep(300);
                    goto menu1;
                    break;
            }
        }
        public static void combotools()
        {
            System.Console.Clear();
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.8 | vx#1234 [<]";
            Console.WriteLine("");
            Ascii();
            Console.WriteLine("");
            System.Console.ForegroundColor = ConsoleColor.DarkCyan;
            Console.WriteLine("");
            prefix("1", "Combo Leecher\n");
            prefix("2", "Combo Editor\n");
            prefix("3", "Proxy Scraper\n");
            prefix("X", "Go Back\n");
            Console.WriteLine("");
            Console.WriteLine("");
            prefix(">", "");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                case "1":
                    {
                        ComboLeecher.Leecher();
                        break;
                    }
                case "2":
                    {
                        comboeditor0();
                        break;
                    }
                case "3":
                    {
                        proxyscraper();
                        break;
                    }
                case "x":
                    {
                        System.Console.Clear();
                        Menu0();
                        break;
                    }
                case "X":
                    {
                        System.Console.Clear();
                        Menu0();
                        break;
                    }
            }
        }
        public static void checkers()
        {
            System.Console.Clear();
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.8 | vx#1234 [<]";
            Console.WriteLine("");
            Ascii();
            Console.WriteLine("");
            System.Console.ForegroundColor = ConsoleColor.DarkCyan;
            Console.WriteLine("");
            prefix("1", "NordVPN\n");
            prefix("2", "Hulu\n");
            prefix("X", "Go Back\n");
            Console.WriteLine("");
            Console.WriteLine("");
            prefix(">", "");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                case "1":
                    {
                        Process.Start(AppDomain.CurrentDomain.BaseDirectory + "Modules/nordvpn.exe");
                        Console.WriteLine("");
                        prefix("+", "Started NordVPN Checker!");
                        Thread.Sleep(1000);
                        Menu0();
                        break;
                    }
                case "2":
                    {
                        Process.Start(AppDomain.CurrentDomain.BaseDirectory + "Modules/hulu.exe");
                        Console.WriteLine("");
                        prefix("+", "Started Hulu Checker!");
                        Thread.Sleep(1000);
                        Menu0();
                        break;
                    }
                case "3":
                    {
                        Console.WriteLine(" ");
                        prefix("!", "Coming Soon!");
                        Thread.Sleep(1500);
                        checkers();
                        break;
                    }
                case "x":
                    {
                        Menu0();
                        break;
                    }
                case "X":
                    {
                        Menu0();
                        break;
                    }
            }
        }
        public static void proxyscraper()
        {
            menu:
            Console.Title =
                "                                                                                                 [>] Shock | Version 1.8 | vx#1234 [<]";
            Console.Clear();
            Program.Ascii();
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine();
            prefix("1", "HTTP\n");
            prefix("2", "SOCKS4\n");
            prefix("3", "SOCKS5\n");
            prefix("X", "Go Back");
            Console.WriteLine("");
            Console.WriteLine("");
            prefix(">", " ");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                case "1":
                    {
                        ProxyScraper.HTTP();
                        break;
                    }
                case "2":
                    {
                        ProxyScraper.SOCKS4();
                        break;
                    }
                case "3":
                    {
                        ProxyScraper.SOCKS5();
                        break;
                    }
                case "X":
                    {
                        System.Console.Clear();
                        combotools();
                        break;
                    }
                case "x":
                    {
                        System.Console.Clear();
                        combotools();
                        break;
                    }
                default:
                    prefix("Invalid Option", "");
                    Thread.Sleep(300);
                    goto menu;
                    break;
            }

        }
        public static void misc()
        {
            menu:
            System.Console.Clear();
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.8 | vx#1234 [<]";
            Console.WriteLine("");
            Ascii();
            Console.WriteLine("");
            Console.WriteLine("");
            prefix("1", "File Sniper\n");
            prefix("X", "Go Back\n");
            Console.WriteLine("");
            Console.WriteLine("");
            prefix(">", "");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                case "1":
                    {
                        filesniper0();
                        break;
                    }
                case "X":
                    {
                        System.Console.Clear();
                        Menu0();
                        break;
                    }
                case "x":
                    {
                        System.Console.Clear();
                        Menu0();
                        break;
                    }
                default:
                    prefix("Invalid Option", "");
                    Thread.Sleep(300);
                    goto menu;
                    break;
            }
        }
        public static void sqltools()
        {
            sql:
            System.Console.Clear();
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.8 | vx#1234 [<]";
            Console.WriteLine("");
            Ascii();
            Console.WriteLine("");
            Console.WriteLine("");
            prefix("1", "Vuln Scanner\n");
            prefix("2", "Dork Parser\n");
            prefix("X", "Go Back\n");
            Console.WriteLine("");
            Console.WriteLine("");
            prefix(">", "");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                case "1":
                    {
                        VulnScanner.Scanner0();
                        break;
                    }
                case "2":
                    {
                        DorkParser.Parser0();
                        break;
                    }
                case "X":
                    {
                        System.Console.Clear();
                        Menu0();
                        break;
                    }
                case "x":
                    {
                        System.Console.Clear();
                        Menu0();
                        break;
                    }
                default:
                    prefix("Invalid Option", "");
                    Thread.Sleep(300);
                    goto sql;
                    break;
            }
        }
        public static void filesniper0()
        {
            sniper:
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.8 | vx#1234 [<]";
            Ascii();
            prefix("1", "Bing\n");
            prefix("2", "Google\n");
            prefix("3", "DuckDuckGo\n");
            prefix("4", "AOL\n");
            prefix("5", "Yahoo\n");
            prefix("X", "Go Back\n");
            Console.WriteLine("");
            Console.WriteLine("");
            prefix("Engine", "");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                case "1":
                    {
                        FileSniper.bing();
                        break;
                    }
                case "2":
                    {
                        FileSniper.google();
                        break;
                    }
                case "3":
                    {
                        FileSniper.duckduckgo();
                        break;
                    }
                case "4":
                    {
                        FileSniper.aol();
                        break;
                    }
                case "5":
                    {
                        FileSniper.yahoo();
                        break;
                    }
                case "X":
                    {
                        System.Console.Clear();
                        misc();
                        break;
                    }
                case "x":
                    {
                        System.Console.Clear();
                        misc();
                        break;
                    }
                default:
                    prefix("Invalid Option", "");
                    Thread.Sleep(300);
                    goto sniper;
                    break;
            }
        }
        public static void comboeditor0()
        {
            comboeditor:
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.8 | vx#1234 [<]";
            System.Console.Clear();
            System.Console.WriteLine();
            Ascii();
            System.Console.WriteLine();
            System.Console.WriteLine();
            prefix("1", "Capture Remover\n");
            prefix("2", "Mail:Pass Edit\n");
            prefix("3", "Dupe Remover\n");
            prefix("4", "Domain Sorter\n");
            prefix("X", "Go Back\n");
            prefix(">", "");
            var Read = System.Console.ReadLine().ToUpper();
            switch (Read)
            {
                case "1":
                    {
                        ComboTool.CaptureRemover();
                        break;
                    }
                case "2":
                    {
                        ComboTool.MailPassEdit();
                        break;
                    }
                case "3":
                    {
                        ComboTool.DupeRemover();
                        break;
                    }
                case "4":
                    {
                        ComboTool.sorter();
                        break;
                    }
                case "X":
                    {
                        System.Console.Clear();
                        combotools();
                        break;
                    }
                case "x":
                    {
                        System.Console.Clear();
                        combotools();
                        break;
                    }
                default:
                    prefix("Invalid Option", "");
                    Thread.Sleep(300);
                    goto comboeditor;
                    break;
            }

        }
    }
}