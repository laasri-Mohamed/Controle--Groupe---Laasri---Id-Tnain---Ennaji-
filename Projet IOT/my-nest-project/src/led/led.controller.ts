import { Controller, Get, Query } from '@nestjs/common';
import { LedService } from './led.service';

@Controller('led')
export class LedController {
  constructor(private readonly ledService: LedService) {}


  @Get('on')
  async turnOnLed(): Promise<{ state: string }> {
    const state = await this.ledService.setLedState('on');
    return { state };
  }

  @Get('off')
  async turnOffLed(): Promise<{ state: string }> {
    const state = await this.ledService.setLedState('off');
    return { state };
  }
}
