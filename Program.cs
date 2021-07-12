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
        }
        public static void Menu0()
        {
            DiscordRPC1.Initialize();
            Export.Initialize();
            menu1:
            System.Console.Clear();
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.2 | vx#1234 [<]";
            Console.WriteLine("");
            Ascii();
            Console.WriteLine("");
            System.Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("");
            prefix("1", "Combo Leecher\n");
            prefix("2", "Combo Editor\n");
            prefix("3", "Proxy Scraper\n");
            prefix("4", "Checkers\n");
            prefix("5", "SQLi Tools\n");
            prefix("6", "Credits\n");
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
                case "4":
                    {
                        checkers();
                        break;
                    }
                case "5":
                    {
                        sqltools();
                        break;
                    }
                case "6":
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
        public static void checkers()
        {
            System.Console.Clear();
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.2 | vx#1234 [<]";
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
                        Process.Start(AppDomain.CurrentDomain.BaseDirectory + "Checkers/nordvpn/nordvpn.exe");
                        Console.WriteLine("");
                        prefix("+", "Started NordVPN Checker!");
                        Thread.Sleep(1000);
                        Menu0();
                        break;
                    }
                case "2":
                    {
                        Process.Start(AppDomain.CurrentDomain.BaseDirectory + "Checkers/hulu/hulu.exe");
                        Console.WriteLine("");
                        prefix("+", "Started Hulu Checker!");
                        Thread.Sleep(1000);
                        Menu0();
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
                "                                                                                                 [>] Shock | Version 1.2 | vx#1234 [<]";
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
                "                                                                                                       [>] Shock | Version 1.2 | vx#1234 [<]";
            Console.WriteLine("");
            Ascii();
            Console.WriteLine("");
            Console.WriteLine("");
            prefix("1", "Vuln Scanner\n");
            prefix("2", "Dork Parser\n");
            prefix("3", "File Sniper (Coming Soon)\n");
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
                case "3":
                    {
                        goto sql;
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
            System.Console.Clear();
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.2 | vx#1234 [<]";
            Console.WriteLine("");
            Ascii();
            Console.WriteLine("");
            Console.WriteLine("");
            prefix("1", "Anonfile\n");
            prefix("2", "Google Drive\n");
            prefix("3", "Zippyshare\n");
            prefix("X", "Go Back\n");
            Console.WriteLine("");
            Console.WriteLine("");
            prefix(">", "");
            var userinput = Console.ReadLine();
            switch (userinput)
            {
                case "1":
                    {
                        FileSniper.anonfile();
                        break;
                    }
                case "2":
                    {
                        FileSniper.drive();
                        break;
                    }
                case "3":
                    {
                        FileSniper.zippyshare();
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
                    goto sniper;
                    break;
            }
        }
        public static void comboeditor0()
        {
            comboeditor:
            Console.Title =
                "                                                                                                       [>] Shock | Version 1.2 | vx#1234 [<]";
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
                    goto comboeditor;
                    break;
            }

        }
    }
}