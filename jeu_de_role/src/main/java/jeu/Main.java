package jeu;

public class Main
{
	static private AppGameContainer app;

	public static void main( String[] args ) throws SlickException
	{
		app = new AppGameContainer( new MyGame() );
		app.setDisplayMode( 640, 480, false );
		app.start();
	}
}