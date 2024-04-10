import java.util.Random;
class StarWars 
{
    private String name;
    private int health;
    private int attack;
    private int defense;
    public StarWars(String name, int health, int attack, int defense) 
    {
        this.name = name;
        this.health = health;
        this.attack = attack;
        this.defense = defense;
    }
    public String getName() 
    {
        return name;
    }
    public int getHealth() 
    {

        return health;
    }
    public int getAttack() 
    {
        return attack;
    }
    public int getDefense() 
    {
        return defense;
    }
    public void reduceHealth(int damage) 
    {
        health -= damage;
        if (health < 0)
        {
            health = 0;
        }
    }
    public boolean isFainted()
    {
        return health == 0;
    }
    public int attack(StarWars opponent) 
    {
        Random rand = new Random();
        int damage = (int) (rand.nextDouble() * attack) - (opponent.getDefense() / 2);
        if (damage < 0) 
        {
            damage = 0;
        }
        opponent.reduceHealth(damage);
        return damage;
    }
}
class Battle 
{
    private StarWars StarWars1;
    private StarWars StarWars2;
    public Battle(StarWars StarWars1, StarWars StarWars2) 
    {
        this.StarWars1 = StarWars1;
        this.StarWars2 = StarWars2;
    }
    public void startBattle() 
    {
        System.out.println("Battle started between " + StarWars1.getName() + " and " + StarWars2.getName());
        while (!StarWars1.isFainted() && !StarWars2.isFainted()) 
        {
            int damage = StarWars1.attack(StarWars2);
            System.out.println(StarWars1.getName() + " attacks " + StarWars2.getName() + " and deals " + damage + " damage.");
            if (StarWars2.isFainted())
            {
                System.out.println(StarWars2.getName() + " fainted. " + StarWars1.getName() + " wins!");
                break;
            }
            damage = StarWars2.attack(StarWars1);
            System.out.println(StarWars2.getName() + " attacks " + StarWars1.getName() + " and deals " + damage + " damage.");
            if (StarWars1.isFainted())
            {
                System.out.println(StarWars1.getName() + " fainted. " + StarWars2.getName() + " wins!");
                break;
            }
        }
    }
}
public class StarWarsBattleArena
{
    public static void main(String[] args) 
    {
        StarWars LukeSywalker = new StarWars("LukeSywalker", 100, 33, 20);
        StarWars DarthVader = new StarWars("DarthVader", 100, 32, 20);
        Battle battle = new Battle(LukeSywalker,DarthVader);
        battle.startBattle();
    }
}