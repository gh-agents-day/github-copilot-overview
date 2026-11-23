using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Net;
using System.Security.Cryptography;
using System.Text;
using System.Web;
using Newtonsoft.Json;

namespace LegacyLibraryReports
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=================================================================");
            Console.WriteLine("  LEGACY .NET FRAMEWORK LIBRARY REPORT GENERATOR (v4.8)");
            Console.WriteLine("=================================================================");

            // 1. Legacy ConfigurationManager from System.Configuration
            string apiUrl = ConfigurationManager.AppSettings["LibraryApiUrl"] ?? "http://127.0.0.1:8000/books";
            string exportPath = ConfigurationManager.AppSettings["ReportExportPath"] ?? "catalog_summary.txt";

            Console.WriteLine($"[Config] Fetching catalog from: {apiUrl}");

            // 2. Deprecated WebClient (Blocking, non-async, synchronous I/O)
            string rawJson = string.Empty;
            try
            {
                using (WebClient client = new WebClient())
                {
                    client.Headers[HttpRequestHeader.ContentType] = "application/json";
                    client.Encoding = Encoding.UTF8;
                    // Obsolete synchronous network download
                    rawJson = client.DownloadString(apiUrl);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[Warning] Unable to connect to live API ({ex.Message}). Using local mock data.");
                rawJson = GetMockJson();
            }

            // 3. Outdated JSON deserialization using legacy Newtonsoft.Json 9.0
            List<BookDto> books = JsonConvert.DeserializeObject<List<BookDto>>(rawJson);

            Console.WriteLine($"\n[Catalog] Total books retrieved: {books?.Count ?? 0}");

            StringBuilder reportBuilder = new StringBuilder();
            reportBuilder.AppendLine("=================================================================");
            reportBuilder.AppendLine("  OFFICIAL LIBRARY CATALOG AUDIT REPORT");
            reportBuilder.AppendLine($"  Generated: {DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")}");
            reportBuilder.AppendLine("=================================================================");

            if (books != null)
            {
                foreach (var book in books)
                {
                    // 4. Deprecated System.Web HttpUtility for URL encoding
                    string encodedTitle = HttpUtility.UrlEncode(book.Title);

                    // 5. Deprecated Cryptography pattern (MD5CryptoServiceProvider / SHA1Managed)
                    string bookChecksum = ComputeMd5Legacy(book.Isbn);

                    reportBuilder.AppendLine($"ISBN: {book.Isbn,-18} | Available: {book.AvailableCopies}/{book.TotalCopies} | Checksum: {bookChecksum.Substring(0, 8)} | Title: {book.Title}");
                }
            }

            // 6. Synchronous File IO
            string directory = Path.GetDirectoryName(exportPath);
            if (!string.IsNullOrEmpty(directory) && !Directory.Exists(directory))
            {
                Directory.CreateDirectory(directory);
            }

            File.WriteAllText(exportPath, reportBuilder.ToString());
            Console.WriteLine($"\n[Success] Report exported to: {Path.GetFullPath(exportPath)}");
            Console.WriteLine("\nContents Preview:\n");
            Console.WriteLine(reportBuilder.ToString());

            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }

        /// <summary>
        /// Legacy MD5 computation using deprecated MD5CryptoServiceProvider
        /// </summary>
        private static string ComputeMd5Legacy(string input)
        {
            if (string.IsNullOrEmpty(input)) return string.Empty;

            using (MD5 md5 = new MD5CryptoServiceProvider())
            {
                byte[] bytes = Encoding.UTF8.GetBytes(input);
                byte[] hash = md5.ComputeHash(bytes);
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < hash.Length; i++)
                {
                    sb.Append(hash[i].ToString("X2"));
                }
                return sb.ToString();
            }
        }

        private static string GetMockJson()
        {
            return @"[
              { ""isbn"": ""978-0132350884"", ""title"": ""Clean Code"", ""author"": ""Robert C. Martin"", ""total_copies"": 5, ""available_copies"": 3 },
              { ""isbn"": ""978-0201616224"", ""title"": ""The Pragmatic Programmer"", ""author"": ""David Thomas"", ""total_copies"": 4, ""available_copies"": 0 },
              { ""isbn"": ""978-0134685991"", ""title"": ""Effective Java"", ""author"": ""Joshua Bloch"", ""total_copies"": 3, ""available_copies"": 2 }
            ]";
        }
    }

    public class BookDto
    {
        [JsonProperty("isbn")]
        public string Isbn { get; set; }

        [JsonProperty("title")]
        public string Title { get; set; }

        [JsonProperty("author")]
        public string Author { get; set; }

        [JsonProperty("total_copies")]
        public int TotalCopies { get; set; }

        [JsonProperty("available_copies")]
        public int AvailableCopies { get; set; }
    }
}
