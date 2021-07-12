using System.Collections.Generic;
using Console = Colorful.Console;
using System.IO;
using System.Net;
using System.Drawing;
using System.Text.RegularExpressions;
using Shock;
using System.Threading;

namespace Shock.Modules
{
	public class FileSniper
	{
		public static void prefix(string prefix, string description)
		{
			Console.Write("    [", Color.White);
			Console.Write(prefix, Color.Cyan);
			Console.Write("] " + description, Color.White);
		}
		public static void anonfile()
        {
			Console.Clear();

			while (true)
			{
				Console.WriteLine("Enter your keyword(s):");
				Console.Write(">");
				string resp = Console.ReadLine();
				int count = 0;
				List<string> Links = new List<string>();
				using (WebClient wc = new WebClient())
				{
					string s = wc.DownloadString("https://google.com/search?q=site:anonfile.com" + resp);
					Regex r = new Regex(@"https:\/\/anonfile.com\/\w+\/\w+");
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
		}
		public static void drive()
		{
			Console.Clear();

			while (true)
			{
				prefix("+", "Enter a keyword");
				Console.WriteLine(" ");
				prefix(">", " ");
				string resp = Console.ReadLine();
				int count = 0;
				List<string> Links = new List<string>();
				using (WebClient wc = new WebClient())
				{
					string s = wc.DownloadString("https://google.com/search?q=site:drive.google.com" + resp);
					Regex r = new Regex(@"https:\/\/drive.google.com\/\w+\/\w+");
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
		}
		public static void zippyshare()
		{
			Console.Clear();

			while (true)
			{
				Console.WriteLine("Enter your keyword(s):");
				Console.Write(">");
				string resp = Console.ReadLine();
				int count = 0;
				List<string> Links = new List<string>();
				using (WebClient wc = new WebClient())
				{
					string s = wc.DownloadString("https://google.com/search?q=site:zippyshare.com" + resp);
					Regex r = new Regex(@"https:\/\/zippyshare.com\/\w+\/\w+");
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
		}
	}
}