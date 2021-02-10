
import java.util.logging.Level;
import java.util.logging.Logger;
import org.newdawn.slick.AppGameContainer;
import org.newdawn.slick.BasicGame;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.SlickException;

public class MyGame extends BasicGame
{
	private GameContainer gc;

	public Game(){
		super( "GameWindow" );
	}

	@Override
	public void init( GameContainer gc ) throws SlickException{
		this.gc = gc;
	}

	@Override
	public void render( GameContainer gc, Graphics g ) throws SlickException{
    g.setColor( Color.white );
	g.drawLine( 100, 150, 300, 350);
	g.setColor( new Color( 128, 128, 128 ) );
	g.drawString( "Basic font test", 0, 0);
	}

	@Override
	public void update( GameContainer gc, int delta ) throws SlickException{
	}
}