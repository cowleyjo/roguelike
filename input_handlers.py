from typing import Optional
import tcod.event

from actions import Action, EscapeAction, MovementAction

class EventHandler:
    def handle_event(self, event: tcod.event.Event) -> Optional[Action]:
        if isinstance(event, tcod.event.KeyDown):
            action: Optional[Action] = None

            key = event.sym

            if key == tcod.event.KeySym.UP:
                return MovementAction(dx=0, dy=-1)
            elif key == tcod.event.KeySym.DOWN:
                return MovementAction(dx=0, dy=1)
            elif key == tcod.event.KeySym.LEFT:
                return MovementAction(dx=-1, dy=0)
            elif key == tcod.event.KeySym.RIGHT:
                return MovementAction(dx=1, dy=0)
            
            elif key == tcod.event.KeySym.ESCAPE:
                return EscapeAction()

            return None
            
        elif isinstance(event, tcod.event.Quit):
            raise SystemExit()
        
        return None
