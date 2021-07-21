using Console = Colorful.Console;
using System.IO;
using System.Net;
using System.Drawing;
using System.Text.RegularExpressions;
using Shock;
using System.Threading;
using System;
using System.Diagnostics;
using Shock.Functions;

namespace Shock.Modules
{
	public class FileSniper
	{
		public static void google()
		{
		start:
			Program.Ascii();
			Program.prefix("1", "Anonfile\n");
			Program.prefix("2", "Google Drive\n");
			Program.prefix("3", "ZippyShare\n");
			Program.prefix("4", "Mediafire\n");
			Program.prefix("5", "Mega\n");
			//Program.prefix("6", "FileIO");
			//Program.prefix("7", "Sendspace");
			var userinput = Console.ReadLine();
			switch (userinput)
			{
				case "1":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://google.com/search?q=site:anonfile.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "2":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://google.com/search?q=site:drive.google.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "3":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://google.com/search?q=site:zippyshare.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "4":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://google.com/search?q=site:mediafire.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "5":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://google.com/search?q=site:mega.nz+" + resp);
							Program.filesniper0();
						}
						break;
					}
				default:
					Program.prefix("!", "Error");
					Thread.Sleep(50);
					goto start;
					break;

			}
		}
		public static void duckduckgo()
		{
		start:
			Program.Ascii();
			Program.prefix("1", "Anonfile\n");
			Program.prefix("2", "Google Drive\n");
			Program.prefix("3", "ZippyShare\n");
			Program.prefix("4", "Mediafire\n");
			Program.prefix("5", "Mega\n");
			//Program.prefix("6", "FileIO");
			//Program.prefix("7", "Sendspace");
			var userinput = Console.ReadLine();
			switch (userinput)
			{
				case "1":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://duckduckgo.com/?q=site:anonfile.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "2":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://duckduckgo.com/?q=site:drive.google.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "3":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://duckduckgo.com/?q=site:zippyshare.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "4":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://duckduckgo.com/?q=site:mediafire.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "5":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://duckduckgo.com/?q=site:mega.nz+" + resp);
							Program.filesniper0();
						}
						break;
					}
				default:
					Program.prefix("!", "Error");
					Thread.Sleep(50);
					goto start;
					break;

			}
		}
		public static void bing()
		{
			start:
			Program.Ascii();
			Program.prefix("1", "Anonfile\n");
			Program.prefix("2", "Google Drive\n");
			Program.prefix("3", "ZippyShare\n");
			Program.prefix("4", "Mediafire\n");
			Program.prefix("5", "Mega\n");
			//Program.prefix("6", "FileIO");
			//Program.prefix("7", "Sendspace");
			var userinput = Console.ReadLine();
			switch (userinput)
			{
				case "1":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://bing.com/search?q=site:anonfile.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "2":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
                        {
							Process.Start("https://bing.com/search?q=site:drive.google.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "3":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
                        {
							Process.Start("https://bing.com/search?q=site:zippyshare.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "4":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://bing.com/search?q=site:mediafire.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "5":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://bing.com/search?q=site:mega.nz+" + resp);
							Program.filesniper0();
						}
						break;
					}
				default:
					Program.prefix("!", "Error");
					Thread.Sleep(50);
					goto start;
					break;

			}
		}
		public static void aol()
		{
		start:
			Program.Ascii();
			Program.prefix("1", "Anonfile\n");
			Program.prefix("2", "Google Drive\n");
			Program.prefix("3", "ZippyShare\n");
			Program.prefix("4", "Mediafire\n");
			Program.prefix("5", "Mega\n");
			//Program.prefix("6", "FileIO");
			//Program.prefix("7", "Sendspace");
			var userinput = Console.ReadLine();
			switch (userinput)
			{
				case "1":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.aol.com/aol/search?q=site:anonfile.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "2":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.aol.com/aol/search?q=site:drive.google.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "3":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.aol.com/aol/search?q=site:zippyshare.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "4":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.aol.com/aol/search?q=site:mediafire.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "5":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.aol.com/aol/search?q=site:mega.nz+" + resp);
							Program.filesniper0();
						}
						break;
					}
				default:
					Program.prefix("!", "Error");
					Thread.Sleep(50);
					goto start;
					break;

			}
		}
		public static void yahoo()
		{
		start:
			Program.Ascii();
			Program.prefix("1", "Anonfile\n");
			Program.prefix("2", "Google Drive\n");
			Program.prefix("3", "ZippyShare\n");
			Program.prefix("4", "Mediafire\n");
			Program.prefix("5", "Mega\n");
			//Program.prefix("6", "FileIO");
			//Program.prefix("7", "Sendspace");
			var userinput = Console.ReadLine();
			switch (userinput)
			{
				case "1":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.yahoo.com/search?q=site:anonfile.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "2":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.yahoo.com/search?q=site:drive.google.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "3":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.yahoo.com/search?q=site:zippyshare.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "4":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.yahoo.com/search?q=site:mediafire.com+" + resp);
							Program.filesniper0();
						}
						break;
					}
				case "5":
					{
						Program.Ascii();
						Console.Write("Keyword: ");
						string resp = Console.ReadLine();
						{
							Process.Start("https://search.yahoo.com/search?q=site:mega.nz+" + resp);
							Program.filesniper0();
						}
						break;
					}
				default:
					Program.prefix("!", "Error");
					Thread.Sleep(50);
					goto start;
					break;

			}
		}
	}
}