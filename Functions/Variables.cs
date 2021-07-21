using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Text;
using Colorful;
using Leaf.xNet;
using System;
using System.Collections.Concurrent;
using System.Linq;
using System.Linq.Expressions;
using System.Net;
using System.Threading;
using Console = Colorful.Console;
using System.Net.Security;
using System.Security.Cryptography.X509Certificates;
using System.Threading.Tasks;
using System.Diagnostics;

namespace Shock.Functions
{
    public class Variables
    {
        public static string Version = "1.6";
        public static string Permission = "y";
        public static string Type = "";
        public static string Folder = "";
        public static int Threads = 250;
        public static int TimeOut = 5000;
        public static int Alive = 0;
        public static int Dead = 0;
        public static List<string> Proxies = new List<string>();
        public static Queue<string> ProxiesQueue = new Queue<string>();
        private static readonly object locker = new object();
        private static readonly object Locked = new object();
        public static string ProxyType { get; set; }
        public static List<string> cloneCombo = new List<string>();
        public static string[] proxies = new string[0];
        public static string mainfolder = Directory.GetCurrentDirectory();
        public static string results;
        public static string subcaps;
        public static bool lines_in_use;
        public static readonly object WriteLock = new object();
        public static string[] OGNAMES;
        public static int Custom_Retries = 1;
        public static string version = "v3.0";
        public static int Valid;
        public static int Custom;
        public static int Errors;
        public static int cps;
        public static int loadedCombos;
        public static int Invalid;
        public static int proxyIndex;
        public static int Checked;
        public static string Module_Name = "";
        public static string Symbol = "";
        public static List<Thread> threads = new List<Thread>();
        public static ConcurrentQueue<string> combos = new ConcurrentQueue<string>();

        // public static string[] accounts;

        //ADDONS
        public static int Rares;
        public static int Skinned;
        public static int No_Skins;
        public static int FN_Hits;
        public static int XBOX_Hits;

        //
        public static string rares;
        public static string skins;
        public static string vbucks;

        // MC
        public static int three_hundred_over;
        public static int two_hundred_to_three_hundred;
        public static int one_hundred_to_two_hundred;
        public static int fifty_to_one_hundred;
        public static int twenty_five_to_fifty;
        public static int ten_to_twentyfive;
        public static int one_to_10;

        public static int MFA;
        public static int NFA;
        public static int SFA;
        public static int Optifine;
        public static int Minecon;
        public static int Hypixel_Lvl;
        public static int Hypixel_Ranked;
        public static int veltpvp;
        public static int Mineplex;
        public static int Skyblock;
        public static int Hive;
        public static int GettingCaptures;
        public static string BASE_NAME = "";

        //folder strings
        public static string Hypixel_Leveled_Folder;
        public static string Hypixel_Ranked_folder;
        public static string VeltPvp_Folder;
        public static string Hive_folder;
        public static string Capes_Folder;
        public static string Skyblock_Coins_Folder;

        public string FilePath { get; set; }
        public static void remove(string Combo)
        {
            if (lines_in_use == true)
            {
                cloneCombo.Remove(Combo);
            }
        }

        public void AppendToFile(string textToAppend)
        {
            var obj = locker;
            lock (obj)
            {
                using (var fileStream = new FileStream(FilePath, FileMode.Append, FileAccess.Write, FileShare.Read))
                {
                    using (var streamWriter = new StreamWriter(fileStream, Encoding.Unicode))
                    {
                        streamWriter.WriteLine(textToAppend);
                    }
                }
            }
        }

        public static void PrintWithPrefix(string prefix, string message, string prefixColour)
        {
            var locked = Locked;
            lock (locked)
            {
                Console.Write("    [", Color.White);
                Console.Write(prefix, Color.Purple);
                Console.WriteLine("] " + message, Color.White);
            }
        }

        public static void PrintWithoutPrefix(string message)
        {
            var locked = Locked;
            lock (locked)
            {
                Console.WriteLine(message, Color.White);
            }
        }
    }
}