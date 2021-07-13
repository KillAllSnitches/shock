using System.Collections.Generic;
using Console = Colorful.Console;
using System.IO;
using System.Net;
using System.Drawing;
using System.Text.RegularExpressions;
using Shock;
using System.Threading;
using System;
using Shock.Functions;

namespace Shock.Modules
{
	public class FileSniper
	{
		public static void anonfile()
        {
			Console.Clear();

			try
			{
				Console.WriteLine("Enter your keyword(s):");
				Console.Write(">");
				string resp = Console.ReadLine();
				int count = 0;
				List<string> Links = new List<string>();
				using (WebClient wc = new WebClient())
				{
					string s = wc.DownloadString("https://google.com/search?q=inurl:anonfile.com+" + resp);
					Regex r0 = new Regex(@"https:\/\/anonfile.com\/\w+\/\w+");
					Regex r1 = new Regex(@"https:\/\/anonfiles.com\//w+\/\w+");
					foreach (Match m in r0.Matches(s))
					{
						count++;
						Links.Add(m.ToString());
					}
					foreach (Match m in r1.Matches(s))
					{
						count++;
						Links.Add(m.ToString());
					}
				}

				using (TextWriter tw = new StreamWriter(@"links.txt"))
				{
					foreach (string line in Links)
					{
						tw.WriteLine(line.ToString());
					}
				}

				Console.WriteLine();
				Console.WriteLine("Scraped " + count.ToString() + " links!" + "|" + "Saved Links to:" + AppDomain.CurrentDomain.BaseDirectory + "links.txt");
				Thread.Sleep(5000);
				Program.Menu0();
			}
            catch
            {
				Console.WriteLine("[!] Your IP is blocked, please change vpn servers or try again later...", Color.Red);
				Thread.Sleep(5000);
				Program.filesniper0();
			}
		}
		public static void drive()
		{
			Console.Clear();

			try
			{
				Program.prefix("+", "Enter a keyword");
				Console.WriteLine(" ");
				Program.prefix(">", " ");
				string resp = Console.ReadLine();
				int count = 0;
				List<string> Links = new List<string>();
				using (WebClient wc = new WebClient())
				{
					string s = wc.DownloadString("https://google.com/search?q=inurl:drive.google.com+" + resp);
					Regex r = new Regex(@"https:\/\/drive.google.com\/drive\/folders\/\w+");
					foreach (Match m in r.Matches(s))
					{
						count++;
						Links.Add(m.ToString());
					}
				}

				using (TextWriter tw = new StreamWriter(@"links.txt"))
				{
					foreach (string line in Links)
					{
						tw.WriteLine(line.ToString());
					}
				}

				Console.WriteLine();
				Console.WriteLine("Scraped " + count.ToString() + " links!");
				Thread.Sleep(500);
				Program.Menu0();
			}
            catch
            {
				Console.WriteLine("[!] Your IP is blocked, please change vpn servers or try again later...", Color.Red);
				Thread.Sleep(5000);
				Program.filesniper0();
			}
		}
	}
}