import { Injectable } from '@nestjs/common';
import axios from 'axios';

@Injectable()
export class LedService {
  private espIp = '128.10.0.92'; // Replace with the actual IP address of your ESP server

  async setLedState(state: 'on' | 'off'): Promise<string> {
    try {
      const response = await axios.get(`http://${this.espIp}/setLedState?state=${state}`);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to set LED state: ${error.message}`);
    }
  }
}
