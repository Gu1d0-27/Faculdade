using Microsoft.EntityFrameworkCore;
using Relacionamentos.Models;

namespace Relacionamentos.Data
{
    public class RelacionamentoContext: DbContext
    {
        public RelacionamentoContext(DbContextOptions<RelacionamentoContext> options): base(options) { }
        public DbSet<Blog> Blogs  { get; set; } 
        public DbSet<Post> Posts { get; set; }
    }
}
