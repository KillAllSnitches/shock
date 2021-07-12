using System;
using System.IO;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Threading;
using Shock.Functions;
using Shock;
using Console = Colorful.Console;

namespace Shock.Modules
{
    public class ProxyScraper
    {
        [STAThread]
        public static void HTTP()
        {
            string[] proxyurls;
            Console.WriteLine("Getting HTTP/S Proxies!");
            proxyurls = new string[6] { "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all", "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt", "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt", "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt", "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt", "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt" };
            WriteProxies(proxyurls, "HTTP");

        } 
        public static void SOCKS4()
        {
            string[] proxyurls;
            Console.WriteLine("Getting SOCKS4 Proxies!");
            proxyurls = new string[4] { "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all", "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt", "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt", "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt" };
            WriteProxies(proxyurls, "Socks4");
        }
        public static void SOCKS5()
        {
            string[] proxyurls;
            Console.WriteLine("Getting SOCKS5 Proxies!");
            proxyurls = new string[4] { "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all", "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt", "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt", "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt" };
            WriteProxies(proxyurls, "Socks5");
        }
        static void WriteProxies(string[] url, string type)
        {
            string filename = type + "_proxies.txt";
            if (File.Exists(filename))
            {
                File.Delete(filename);
            }
            WebClient webClient = new WebClient();
            webClient.Timeout = 5000;
            string proxylist = "";
            string[] proxyarray = url;
            foreach (string proxyurl in proxyarray)
            {
                proxylist = proxylist + webClient.DownloadString(proxyurl) + Environment.NewLine;
            }
            using (StreamWriter writer = new StreamWriter(filename))
            {
                writer.Write(proxylist);
            }
            Console.Clear();
            int lineCount = File.ReadLines(filename).Count();
            Console.WriteLine("Exported " + lineCount + " proxies to: " + AppDomain.CurrentDomain.BaseDirectory + filename);
            Thread.Sleep(300);
            Program.proxyscraper();
        }
        private class WebClient : System.Net.WebClient
        {
            public int Timeout { get; set; }
            protected override WebRequest GetWebRequest(Uri uri)
            {
                WebRequest lWebRequest = base.GetWebRequest(uri);
                lWebRequest.Timeout = Timeout;
                ((HttpWebRequest)lWebRequest).ReadWriteTimeout = Timeout;
                return lWebRequest;
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
      