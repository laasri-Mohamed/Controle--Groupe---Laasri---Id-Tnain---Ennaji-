import { HttpModule } from '@nestjs/axios';
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { LedController } from './led/led.controller';
import { LedService } from './led/led.service';

@Module({
  imports: [HttpModule],
  controllers: [AppController, LedController],
  providers: [AppService, LedService],
})
export class AppModule {}
