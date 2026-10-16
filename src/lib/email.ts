import { Resend } from 'resend';

export interface BaseInquiryData {
  type: 'general' | 'contact-page' | 'durga-puja';
  name?: string;
  organization?: string;
  category?: string;
  solutionType?: string;
  contactMethod: 'WhatsApp' | 'Email' | 'Phone';
  contactValue: string;
  requirementNote?: string;
  // Durga Puja specific fields
  committeeName?: string;
  zone?: string;
  contactPerson?: string;
  designation?: string;
  selectedPriorities?: string[];
  estimatedFootfall?: string;
  notes?: string;
}

export interface SendResult {
  success: boolean;
  id?: string;
  deliveredTo: string;
  isFallback: boolean;
  message?: string;
}

function escapeHtml(text: string): string {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

export function generateInquiryHtml(data: BaseInquiryData, isFallback = false): string {
  const isPuja = data.type === 'durga-puja';
  const title = isPuja
    ? 'Durga Puja Sharodotsav 2026 Inquiry'
    : data.type === 'contact-page'
    ? 'Direct Contact Brief'
    : 'Studio Consultation Request';

  const clientName = isPuja
    ? data.contactPerson || 'Committee Representative'
    : data.name || 'Website Visitor';

  const clientOrg = isPuja
    ? data.committeeName || 'Puja Committee'
    : data.organization || 'Independent Client';

  const category = isPuja ? data.zone || 'Kolkata Zone' : data.category || 'Growing Business';
  const requirement = isPuja ? data.notes : data.requirementNote;

  // Generate Quick Action URL
  let actionButton = '';
  if (data.contactMethod === 'WhatsApp') {
    const cleanNum = data.contactValue.replace(/[^0-9]/g, '');
    const waUrl = `https://wa.me/${cleanNum.startsWith('91') ? cleanNum : '91' + cleanNum}`;
    actionButton = `<a href="${waUrl}" style="display:inline-block;padding:10px 18px;background-color:#22c55e;color:#ffffff;text-decoration:none;border-radius:6px;font-weight:600;font-size:14px;margin-top:10px;">Chat on WhatsApp &rarr;</a>`;
  } else if (data.contactMethod === 'Email') {
    actionButton = `<a href="mailto:${escapeHtml(data.contactValue)}" style="display:inline-block;padding:10px 18px;background-color:#0284c7;color:#ffffff;text-decoration:none;border-radius:6px;font-weight:600;font-size:14px;margin-top:10px;">Reply via Email &rarr;</a>`;
  } else if (data.contactMethod === 'Phone') {
    actionButton = `<a href="tel:${escapeHtml(data.contactValue)}" style="display:inline-block;padding:10px 18px;background-color:#0284c7;color:#ffffff;text-decoration:none;border-radius:6px;font-weight:600;font-size:14px;margin-top:10px;">Call Client &rarr;</a>`;
  }

  const fallbackBanner = isFallback
    ? `
    <div style="background-color:#fef3c7;border-left:4px solid #f59e0b;padding:12px 16px;margin-bottom:24px;border-radius:4px;color:#92400e;font-size:13px;line-height:1.5;">
      <strong>⚠️ Testing Sandbox Notice:</strong> Delivered to your verified account email because <code>techzyan.org</code> domain is pending verification in Resend. Once verified at <a href="https://resend.com/domains" style="color:#b45309;font-weight:600;">resend.com/domains</a>, incoming inquiries will route straight to <code>contact@techzyan.org</code>.
    </div>
  `
    : '';

  return `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>${escapeHtml(title)}</title>
</head>
<body style="margin:0;padding:24px;background-color:#0b0f19;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:#e2e8f0;">
  <div style="max-width:620px;margin:0 auto;background-color:#111827;border:1px solid #1f2937;border-radius:12px;overflow:hidden;box-shadow:0 10px 25px rgba(0,0,0,0.5);">
    
    <!-- Header -->
    <div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%);padding:24px 30px;border-bottom:1px solid #334155;">
      <div style="color:#38bdf8;font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:6px;">
        Techzyan Technical Studio
      </div>
      <h1 style="margin:0;font-size:22px;color:#f8fafc;font-weight:700;">
        ${escapeHtml(title)}
      </h1>
      <div style="color:#94a3b8;font-size:13px;margin-top:4px;">
        Received on ${new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })} IST
      </div>
    </div>

    <!-- Content -->
    <div style="padding:28px 30px;">
      ${fallbackBanner}

      <!-- Client Details Grid -->
      <table style="width:100%;border-collapse:collapse;margin-bottom:20px;">
        <tr>
          <td style="padding:8px 0;color:#94a3b8;font-size:13px;width:35%;border-bottom:1px solid #1f2937;"><strong>Client / Sender:</strong></td>
          <td style="padding:8px 0;color:#f8fafc;font-size:14px;border-bottom:1px solid #1f2937;">${escapeHtml(clientName)}</td>
        </tr>
        <tr>
          <td style="padding:8px 0;color:#94a3b8;font-size:13px;border-bottom:1px solid #1f2937;"><strong>Organization / Entity:</strong></td>
          <td style="padding:8px 0;color:#f8fafc;font-size:14px;border-bottom:1px solid #1f2937;">${escapeHtml(clientOrg)}</td>
        </tr>
        <tr>
          <td style="padding:8px 0;color:#94a3b8;font-size:13px;border-bottom:1px solid #1f2937;"><strong>Category / Sector:</strong></td>
          <td style="padding:8px 0;color:#38bdf8;font-size:14px;font-weight:600;border-bottom:1px solid #1f2937;">${escapeHtml(category)}</td>
        </tr>
        ${
          data.solutionType
            ? `<tr>
                <td style="padding:8px 0;color:#94a3b8;font-size:13px;border-bottom:1px solid #1f2937;"><strong>Solution Requested:</strong></td>
                <td style="padding:8px 0;color:#f8fafc;font-size:14px;border-bottom:1px solid #1f2937;">${escapeHtml(data.solutionType)}</td>
              </tr>`
            : ''
        }
        ${
          data.designation
            ? `<tr>
                <td style="padding:8px 0;color:#94a3b8;font-size:13px;border-bottom:1px solid #1f2937;"><strong>Designation:</strong></td>
                <td style="padding:8px 0;color:#f8fafc;font-size:14px;border-bottom:1px solid #1f2937;">${escapeHtml(data.designation)}</td>
              </tr>`
            : ''
        }
        ${
          data.selectedPriorities && data.selectedPriorities.length > 0
            ? `<tr>
                <td style="padding:8px 0;color:#94a3b8;font-size:13px;border-bottom:1px solid #1f2937;"><strong>Requested Priorities:</strong></td>
                <td style="padding:8px 0;color:#f8fafc;font-size:14px;border-bottom:1px solid #1f2937;">${escapeHtml(data.selectedPriorities.join(', '))}</td>
              </tr>`
            : ''
        }
        ${
          data.estimatedFootfall
            ? `<tr>
                <td style="padding:8px 0;color:#94a3b8;font-size:13px;border-bottom:1px solid #1f2937;"><strong>Estimated Footfall:</strong></td>
                <td style="padding:8px 0;color:#f8fafc;font-size:14px;border-bottom:1px solid #1f2937;">${escapeHtml(data.estimatedFootfall)}</td>
              </tr>`
            : ''
        }
        <tr>
          <td style="padding:8px 0;color:#94a3b8;font-size:13px;border-bottom:1px solid #1f2937;"><strong>Preferred Contact Channel:</strong></td>
          <td style="padding:8px 0;color:#f8fafc;font-size:14px;border-bottom:1px solid #1f2937;">${escapeHtml(data.contactMethod)}</td>
        </tr>
        <tr>
          <td style="padding:8px 0;color:#94a3b8;font-size:13px;border-bottom:1px solid #1f2937;"><strong>Contact Detail:</strong></td>
          <td style="padding:8px 0;color:#f8fafc;font-size:14px;font-weight:600;border-bottom:1px solid #1f2937;">
            ${escapeHtml(data.contactValue)}
            ${actionButton ? `<br>${actionButton}` : ''}
          </td>
        </tr>
      </table>

      <!-- Project Requirement / Message -->
      <div style="background-color:#0f172a;border:1px solid #1e293b;border-radius:8px;padding:16px;margin-top:20px;">
        <div style="font-size:12px;font-weight:700;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">
          Requirement Notes &amp; Scope:
        </div>
        <div style="color:#e2e8f0;font-size:14px;line-height:1.6;white-space:pre-wrap;">${
          requirement ? escapeHtml(requirement) : '<em style="color:#64748b;">No additional notes provided.</em>'
        }</div>
      </div>

    </div>

    <!-- Footer -->
    <div style="background-color:#0f172a;padding:16px 30px;border-top:1px solid #1f2937;font-size:12px;color:#64748b;text-align:center;">
      This email was automatically dispatched by the Techzyan website inquiry system.<br>
      Direct inquiries: <a href="mailto:contact@techzyan.org" style="color:#38bdf8;text-decoration:none;">contact@techzyan.org</a> | +91-7439303013
    </div>

  </div>
</body>
</html>
  `.trim();
}

export function generateInquiryText(data: BaseInquiryData): string {
  const isPuja = data.type === 'durga-puja';
  const title = isPuja
    ? 'Durga Puja Sharodotsav 2026 Inquiry'
    : data.type === 'contact-page'
    ? 'Direct Contact Brief'
    : 'Studio Consultation Request';

  const clientName = isPuja
    ? data.contactPerson || 'Committee Representative'
    : data.name || 'Website Visitor';

  const clientOrg = isPuja
    ? data.committeeName || 'Puja Committee'
    : data.organization || 'Independent Client';

  const lines = [
    `TECHZYAN TECHNICAL STUDIO — ${title.toUpperCase()}`,
    `----------------------------------------------------`,
    `Date: ${new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' })} IST`,
    `Name: ${clientName}`,
    `Organization: ${clientOrg}`,
    `Category: ${isPuja ? data.zone || 'Kolkata Zone' : data.category || 'Growing Business'}`,
    data.solutionType ? `Solution Requested: ${data.solutionType}` : null,
    data.designation ? `Designation: ${data.designation}` : null,
    data.selectedPriorities ? `Priorities: ${data.selectedPriorities.join(', ')}` : null,
    data.estimatedFootfall ? `Footfall: ${data.estimatedFootfall}` : null,
    `Preferred Channel: ${data.contactMethod}`,
    `Contact Value: ${data.contactValue}`,
    `----------------------------------------------------`,
    `Requirement Note:`,
    isPuja ? data.notes || 'None' : data.requirementNote || 'None',
    `----------------------------------------------------`,
  ].filter(Boolean);

  return lines.join('\n');
}

export async function sendInquiryEmail(data: BaseInquiryData): Promise<SendResult> {
  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    throw new Error('RESEND_API_KEY is not configured in environment variables');
  }

  const resend = new Resend(apiKey);

  const primaryRecipient = process.env.CONTACT_RECIPIENT_EMAIL || 'contact@techzyan.org';
  const fallbackRecipient = process.env.FALLBACK_RECIPIENT_EMAIL || 'samudraganguly002017@gmail.com';
  const fromSender = process.env.RESEND_FROM_EMAIL || 'Techzyan Studio <onboarding@resend.dev>';

  const subjectPrefix = data.type === 'durga-puja'
    ? '[Puja 2026 Inquiry]'
    : '[Website Inquiry]';

  const clientIdentifier = (data.name || data.contactPerson || data.organization || data.committeeName || 'New Client').trim();
  const subject = `${subjectPrefix} ${clientIdentifier} (${data.category || data.zone || 'Consultation'})`;

  // Set reply-to if contact method is email
  const replyTo = data.contactMethod === 'Email' && data.contactValue.includes('@')
    ? data.contactValue.trim()
    : undefined;

  // 1. Try sending to primary recipient (contact@techzyan.org)
  try {
    const response = await resend.emails.send({
      from: fromSender,
      to: [primaryRecipient],
      replyTo,
      subject,
      html: generateInquiryHtml(data, false),
      text: generateInquiryText(data),
    });

    if (response.error) {
      throw response.error;
    }

    return {
      success: true,
      id: response.data?.id,
      deliveredTo: primaryRecipient,
      isFallback: false,
    };
  } catch (err: any) {
    const errorMessage = String(err?.message || err || '');
    console.warn(`[Resend Primary Send Failed] To: ${primaryRecipient}. Reason:`, errorMessage);

    // If error indicates unverified domain or test account restriction, fallback to account owner email
    const isDomainOrSandboxError =
      errorMessage.includes('You can only send testing emails to your own email address') ||
      errorMessage.includes('is not verified') ||
      errorMessage.includes('validation_error');

    if (isDomainOrSandboxError && fallbackRecipient && fallbackRecipient !== primaryRecipient) {
      console.info(`[Resend Fallback Triggered] Retrying to account owner: ${fallbackRecipient}`);

      const fallbackResponse = await resend.emails.send({
        from: 'Techzyan Studio <onboarding@resend.dev>',
        to: [fallbackRecipient],
        replyTo,
        subject: `[Sandbox Notice] ${subject}`,
        html: generateInquiryHtml(data, true),
        text: `[Delivered to ${fallbackRecipient} because techzyan.org domain verification is pending in Resend]\n\n` + generateInquiryText(data),
      });

      if (fallbackResponse.error) {
        throw new Error(`Resend send failed: ${fallbackResponse.error.message}`);
      }

      return {
        success: true,
        id: fallbackResponse.data?.id,
        deliveredTo: fallbackRecipient,
        isFallback: true,
        message: 'Delivered to registered Resend account owner while custom domain verification is pending.',
      };
    }

    throw new Error(errorMessage || 'Failed to dispatch email via Resend');
  }
}
