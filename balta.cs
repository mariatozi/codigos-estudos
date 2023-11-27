using System;
using System.Security.Cryptography.X509Certificates;

///importanções (definidas pelo using)

namespace Teste /// divisões lógicas de arquivos
{
	class Program /// programa em si(classe) - tudo que será executado
	{
		static void Main(string[] args) /// método main(principal)
		{ 
			// instanciar uma estrutura
			var mouse = new Product(1, "Mouse Gamer", 299.97, EProductType.Product);
			var manutencaoEletrica = new Product(2, "Manutenção elétrica", 500, EProductType.Service);
			
			mouse.Id = 55; // sobescrever qualquer valor

			Console.WriteLine(mouse.Id);
			Console.WriteLine(mouse.Name);
			Console.WriteLine(mouse.Price);
			Console.WriteLine(mouse.Type);
		}
	}

	struct Product 
	{
		public Product(int id, string name, double price, EProductType type)
		{
			Id = id;
			Name = name;
			Price = price;
			Type = type;
		}

		public int Id;
		public string Name;
		public double Price;
		public EProductType Type;

		public double PriceInDolar(double dolar) 
		{
			return Price * dolar;
		}
	}

	enum EProductType 
	{
		Product = 1,
		Service = 2
	}
}
