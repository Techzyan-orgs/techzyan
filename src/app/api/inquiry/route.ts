import { NextRequest, NextResponse } from 'next/server';
import { sendInquiryEmail, BaseInquiryData } from '@/lib/email';

export async function POST(req: NextRequest) {
  try {
    const body = (await req.json()) as BaseInquiryData;

    if (!body || !body.contactMethod || !body.contactValue) {
      return NextResponse.json(
        {
          success: false,
          error: 'Missing required contact information (contactMethod and contactValue are required).',
        },
        { status: 400 }
      );
    }

    const result = await sendInquiryEmail(body);

    return NextResponse.json(result, { status: 200 });
  } catch (error: any) {
    console.error('API /api/inquiry error:', error);
    return NextResponse.json(
      {
        success: false,
        error: error?.message || 'Internal server error while dispatching email notification.',
      },
      { status: 500 }
    );
  }
}
