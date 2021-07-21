using DiscordRPC;

namespace Shock.Functions
{
    internal class DiscordRPC1
    {
        public static DiscordRpcClient client;

        public static void Initialize()
        {
            client = new DiscordRpcClient("863572690447106078");
            client.Initialize();
            client.SetPresence(new RichPresence
            {
                Details = "discord.io/shockaio",
                State = "Version 1.7",
                Timestamps = Timestamps.Now,
                Assets = new Assets
                {
                    LargeImageKey = "logo",
                    LargeImageText = "Shock Multi-Tool"
                }
            });
        }
    }
}